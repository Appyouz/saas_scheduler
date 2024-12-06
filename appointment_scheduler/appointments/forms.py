from django import forms
from .models import Appointment, Business

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['business', 'customer_name', 'service', 'date_time', 'status']
    
    # Optional: Add validation to ensure no double bookings happen
    def clean_date_time(self):
        date_time = self.cleaned_data['date_time']
        # Ensure no existing appointments overlap
        if Appointment.objects.filter(date_time=date_time).exists():
            raise forms.ValidationError('This time is already booked, please choose another one.')
        return date_time
