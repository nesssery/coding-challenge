from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from stores.forms import CustomCreationModel3DForm
from stores.models import Model3d, UserBadge
from django.db.models import Sum
from django.contrib.auth.models import User
from users.models import CustomUser
def handler404view(request, exception):
    return render(request, 'pages/404.html', status=404)

def handler500view(request, *args, **argv):
    return render(request, 'pages/500.html', status=500)

class HomeView(View):
    def get(self, request):
        model3dObjects = Model3d.objects.all()
        userBadgeObjects = UserBadge.objects.all()
        userBadges = UserBadge.objects.all()
       
        context = {
            "model3dObjects": model3dObjects,
            "userBadgeObjects": userBadgeObjects,
            "userBadges": userBadges,
        }
        return render(request, 'pages/home.html', context)



class DetailView(View):
    def get(self, request, pk):
        latestObjects = Model3d.objects.all().order_by('-dateAdded')[:3]
        Model3dObject = Model3d.objects.get(id=pk)
        userBadgeObjects = UserBadge.objects.all()
        Model3dObject.views = Model3dObject.views + 1
        Model3dObject.save()
        return render(request, "pages/detail.html", {
            'Model3d': Model3dObject,
            "latestObjects": latestObjects,
            "userBadgeObjects": userBadgeObjects
        })



class EditorView(View):
    def get(self, request):
        form = CustomCreationModel3DForm()
        context = {'form': form}
        return render(request, 'pages/page-editor.html', context)

    def post(self, request):
        form = CustomCreationModel3DForm(request.POST, request.FILES)
        user = request.user
        if form.is_valid():
            model3d_title = form.cleaned_data['title']
            model3d_description = form.cleaned_data['description']
            model3d_image = form.cleaned_data['image']
            new_article = Model3d(title=model3d_title, image=model3d_image, description=model3d_description, user=user)
            new_article.save()
            return redirect('/')
        else:
            print(form.errors)
        context = {'form': form}
        return render(request, 'pages/page-editor.html', context)


