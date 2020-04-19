from django.shortcuts import render
from django.http import Http404

def home(request):
	import json, requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=2B9A0408-5CAD-4813-85D5-E23484BED4BB")
		#pi_request.raise_for_status()
		try:
			api = json.loads(api_request.content)
		except:
			api = "another error...."

		#raise Http404("request failed")
		#the pythonic way of accessing the dict
		#the html or diango way is api.0.Category.Name (0 for the item of the api response and the subsequent names are the keys to access whatever value ur looking for)	

		if len(api) > 0:
			if (api[0]['Category']['Name'] == "Good"):
				category_description = "(0 - 50) Air quality acceptable and air polution poses no risk"
				category_color = "good"
			elif (api[0]['Category']['Name'] == "Moderate"):
				category_description = "(51 - 100) Air Quality is still acceptable - but some pulltants may put you at risk"
				category_color = "moderate"
			elif (api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups"):
				category_description = "(101 - 150) People with lung / heart conditions or the elderly may be at risk!"
				category_color = "usg"
			elif (api[0]['Category']['Name'] == "Unhealthy"):
				category_description = "(151 - 200) Everyone may beggin to experience health effects."
				category_color = "unhealthy"
			elif (api[0]['Category']['Name'] == "Very Unhealthy"):
				category_description = "(201 - 300) You are in the danger zone! Exposure may lead to serious health effects"
				category_color = "veryunhealthy"
			elif (api[0]['Category']['Name'] == "Hazardous"):
				category_description = "(301 - 500) RUN FOR YOUR LIFE!!!"
				category_color = "unhealthy"
		else:
			api = "ERROR"
			category_description = "Zip Code '" +zipcode+"' invalid or not found. Plase try something else "
			category_color = "badRequest"
			
		return render(request, 'home.html',{'api':api,'category_description':category_description,'category_color':category_color})

	else:		
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=2B9A0408-5CAD-4813-85D5-E23484BED4BB")
		try:
			api = json.loads(api_request.content)

		except Exception as e:
			api = "Something went wrong..."
			#raise Http404("request failed")
		#the pythonic way of accessing the dict
		#the html or diango way is api.0.Category.Name (0 for the item of the api response and the subsequent names are the keys to access whatever value ur looking for)	
		if (api[0]['Category']['Name'] == "Good"):
			category_description = "(0 - 50) Air quality acceptable and air polution poses no risk"
			category_color = "good"
		elif (api[0]['Category']['Name'] == "Moderate"):
			category_description = "(51 - 100) Air Quality is still acceptable - but some pulltants may put you at risk"
			category_color = "moderate"
		elif (api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups"):
			category_description = "(101 - 150) People with lung / heart conditions or the elderly may be at risk!"
			category_color = "usg"
		elif (api[0]['Category']['Name'] == "Unhealthy"):
			category_description = "(151 - 200) Everyone may beggin to experience health effects."
			category_color = "unhealthy"
		elif (api[0]['Category']['Name'] == "Very Unhealthy"):
			category_description = "(201 - 300) You are in the danger zone! Exposure may lead to serious health effects"
			category_color = "veryunhealthy"
		elif (api[0]['Category']['Name'] == "Hazardous"):
			category_description = "(301 - 500) RUN FOR YOUR LIFE!!!"
			category_color = "hazardous"

	  

	return render(request, 'home.html',
		{'api':api,
		'category_description': category_description, 
		'category_color': category_color})
	#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=2B9A0408-5CAD-4813-85D5-E23484BED4BB



def about(request):
	return render(request, 'about.html',{})