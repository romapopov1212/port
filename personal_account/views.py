from django.shortcuts import render, redirect
from user.views import checkingNameEmail
from .models import Achievement
from .models import Certificates

class AchievementCertificates:
    def __init__(self, nameAchievement, eventName, link, points, certificates):
        self.nameAchievement = nameAchievement
        self.eventName = eventName
        self.link = link
        self.certificates = certificates
        self.points = points
        
    
def profile(request):
    if request.POST:
        return render(request, 'editProfile.html')
    
    achievement = Achievement.objects.filter(user=request.user)
    achievements = []
    for i in achievement:
        certificates = Certificates.objects.filter(achievement=i.id)
        achievements.append(AchievementCertificates(i.name_achievement, i.event_name, i.link, i.points, certificates))
    
    context = {
        'page_obj': achievements
    }
    return render(request, 'profile.html', context=context)

def editProfile(request):
    if request.POST:
        email = request.POST.get('email')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        img = request.FILES.get('image')
        if not checkingNameEmail(request, email, name) and (email != request.user.email 
                                                            or name != request.user.name):
            return redirect('personal_account:edit_profile')

        request.user.name = name
        request.user.email = email
        request.user.phone = phone
        request.user.image = img
        request.user.about_me = request.POST.get('aboutMe')
        request.user.save()
        return redirect('personal_account:profile')
    
    return render(request, 'editProfile.html')

def addAchievement(request):
    if request.POST:
        name = request.POST.get('achievementName')
        eventName = request.POST.get('eventName')
        link = request.POST.get('link')
        imgs = request.FILES.getlist('images')
        achievement = Achievement(name_achievement=name, event_name=eventName, link=link, user=request.user)
        achievement.save()
        
        for i in imgs:
            certificates = Certificates(image=i, achievement=achievement)
            certificates.save()

    return render(request, 'addAchievement.html')

# def verify_achievement(request, achievement_id):
#     if not request.user.is_staff:
#         return redirect('home')

#     achievement = Achievement.objects.filter(id=achievement_id)
#     if request.method == 'POST':
#         status = request.POST.get('status')
#         if status in dict(Achievement.STATUS_CHOICES).keys():
#             achievement.status = status
#             achievement.save()
#         return redirect('admin_achievement_list')

#     return render(request, 'verify_achievement.html', {'achievement': achievement})