from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    orders = profile.get_order_history()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    context = {
        'form': form,
        'orders': orders,
    }
    return render(request, 'profiles/profile.html', context)
