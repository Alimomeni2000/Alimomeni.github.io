from .models import SocialMedia

def social_media_links(request):
    social_medias = SocialMedia.objects.all()
    return {'social_medias': social_medias}
