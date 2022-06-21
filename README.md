# Login-Template-Django

Simple login, logout, registration applications to add to your project. Uses LoginRequiredMixin and login decorator to autheticate who can edit, update, delete, and/or view certain pages.

## Important 
<ul>
  <li>In settings.py, make sure to give location values to LOGIN_REDIRECT_URL and LOGOUT_REDIRECT_URL in order for the login, logout system to work properly.</li>
  <li>Add the @login_required above your home html file view. And add LoginRequiredMixin to your arguments in views classes to enforce the login requirement.</li> 
</ul>
