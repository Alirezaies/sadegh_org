from django.shortcuts import render

def error_404(request, exception):
    data = {
        'lead_message':'Not Found',
        'message':'This requested URL was not found on this server.',
        'status_code': 404,
        'ref': request.META.get('HTTP_REFERER')
    }

    return render(request, 'admin/errors/404.html', data, status=404)

def error_403(request, exception):
    data = {
        'lead_message':'Unauthorized',
        'message':'Access to this resource is denied.',
        'status_code': 403,
        'ref': request.META.get('HTTP_REFERER')
    }

    return render(request, 'admin/errors/error.html', data, status=403)

def error_500(request):
    data = {
        'lead_message':'Internal Server Error',
        'message':'There Is Back-End Error',
        'status_code': 500,
        'ref': request.META.get('HTTP_REFERER')
    }

    return render(request, 'admin/errors/400.html', data, status=500)
