from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .models import ChosenFont
from .models import FontEntry
import copy

@login_required
def index(request):
    context = RequestContext(request)
    context_dict = dict()

    font_entries = FontEntry.objects.all()
    chosen_fonts = ChosenFont.objects.all()

    html_file = open('/tmp/fonts.html','w')
    for font in chosen_fonts:
        formatted_font_name = str(font.font_entry)
        formatted_font_name = formatted_font_name.replace(' ','+')
        html_file.write("<link href=\'http://fonts.googleapis.com/css?family=")
        html_file.write(formatted_font_name)
        html_file.write("\' rel=\'stylesheet\' type=\'text/css\'>\n\n")

    html_file.close()

    css_file = open('../static/css/fonts.css','w')
    for font in chosen_fonts:
        formatted_font_name = str(font.font_entry)
        formatted_font_name = formatted_font_name.replace(' ','+')
        css_file.write("@import url(http://fonts.googleapis.com/css?family=")
        css_file.write(formatted_font_name)
        css_file.write(");\n\n")
        css_file.write(".")
        css_file.write(font.font_class)
        css_file.write("\n")
        css_file.write("{")
        css_file.write("\n")
        # get font
        css_file.write('\t')
        css_file.write("font-family: '")
        css_file.write(str(font.font_entry))
        css_file.write("';\n")

        # get color 
        css_file.write('\t')
        css_file.write("color: #")
        css_file.write(str(font.color))
        css_file.write(";\n")

 
        # get size 
        css_file.write('\t')
        css_file.write("size: ")
        css_file.write(str(font.size))
        css_file.write("px;\n")


        
        css_file.write("}")
        css_file.write("\n")
        css_file.write("\n")

    css_file.close()
    css_file = open('../static/css/fonts.css')
    css_file_data = css_file.read()
    html_file = open('/tmp/fonts.html')
    html_file_data = html_file.read()
    context_dict['css_file_data'] = css_file_data
    context_dict['html_file_data'] = html_file_data

    return render_to_response('fonts.css', context_dict, context)
