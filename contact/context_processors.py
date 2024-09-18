from .models import Information_Contact


def contacts(request):
    return {
        'index_contacts': Information_Contact.objects.first()
    }