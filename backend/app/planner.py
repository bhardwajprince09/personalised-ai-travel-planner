import json
# budget match
b = prefs.get('budget','moderate')
if b == 'budget' and poi.price in ['free','cheap']:
score += 1
if b == 'luxury' and poi.price in ['expensive']:
score += 1
# rating
score += poi.rating / 2.0
return score




def travel_time_minutes(a, b):
try:
return int(geodesic((a.lat,a.lon),(b.lat,b.lon)).km / 30 * 60) # assume avg 30 km/h urban
except Exception:
return 20




def generate_itineraries(trip_request: dict):
prefs = trip_request.get('preferences', {})
dest = trip_request.get('destination','')
candidates = [p for p in POIS if dest.lower() in p.city.lower()]
if not candidates:
candidates = POIS
scored = [(p, score_poi(p,prefs)) for p in candidates]
scored.sort(key=lambda x: x[1], reverse=True)
top = [p for p,_ in scored[:20]]


start = datetime.fromisoformat(trip_request['start_date'])
end = datetime.fromisoformat(trip_request['end_date'])
days = max(1,(end - start).days + 1)


itineraries = []
for option in range(1):
it = { 'option_id': f'opt_{option+1}', 'days': [] }
idx = 0
for d in range(days):
day_date = (start + timedelta(days=d)).date().isoformat()
slots = {'morning': None, 'afternoon': None, 'evening': None}
for slot in slots:
if idx >= len(top): break
poi = top[idx]
slots[slot] = {
'id': poi.id,
'name': poi.name,
'duration_mins': 90,
'tags': poi.tags,
'coords': [poi.lat, poi.lon]
}
idx += 1
it['days'].append({'date': day_date, 'slots': slots})
itineraries.append(it)
return itineraries
