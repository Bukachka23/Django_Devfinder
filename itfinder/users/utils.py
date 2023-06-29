from .models import Profile, Skill
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

# This function is used for pagination
def paginateProfiles(request, profiles, results):
    page = request.GET.get('page')
    paginator = Paginator(profiles, results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    # Calculate the indices for the pages to display in the paginator
    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, profiles

# This function is used for searching profiles based on a query
def searchProfiles(request):
    # It retrieves the search query from the query string of the URL
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    # Search Skills model for any skills that contain the search query
    skills = Skill.objects.filter(name__icontains=search_query)
    # Search Profiles model for any profiles where the name or intro contains the search query, or the profile has one of the skills found earlier
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(intro__icontains=search_query) |
        Q(skills__in=skills)
    )
    return profiles, search_query