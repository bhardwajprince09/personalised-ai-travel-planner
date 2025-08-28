import React, {useState} from 'react'
import axios from 'axios'
import Itinerary from './components/Itinerary'


export default function App(){
const [destination,setDestination] = useState('Kyoto')
const [start,setStart] = useState('2025-10-15')
const [end,setEnd] = useState('2025-10-17')
const [budget,setBudget] = useState('moderate')
const [itineraries,setItineraries] = useState([])


async function plan(){
try{
const res = await axios.post('/api/trips', {
destination,start_date:start,end_date:end,budget,preferences:{interests:['culture','food'],budget}
})
setItineraries(res.data.itineraries)
}catch(e){
// try full backend URL fallback
try{
const res = await axios.post('http://localhost:8000/api/trips', {
destination,start_date:start,end_date:end,budget,preferences:{interests:['culture','food'],budget}
})
setItineraries(res.data.itineraries)
}catch(err){
alert('Failed to contact backend. Check console for errors.')
console.error(err)
}
}
}


return (
<div className="min-h-screen p-6 font-sans">
<h1 className="text-2xl mb-4">Personalized AI Travel Planner — MVP</h1>
<div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
<input value={destination} onChange={e=>setDestination(e.target.value)} />
<input type="date" value={start} onChange={e=>setStart(e.target.value)} />
<input type="date" value={end} onChange={e=>setEnd(e.target.value)} />
<select value={budget} onChange={e=>setBudget(e.target.value)}>
<option value="budget">Budget</option>
<option value="moderate">Moderate</option>
<option value="luxury">Luxury</option>
</select>
</div>
<button onClick={plan} className="px-4 py-2 rounded bg-blue-600 text-white">Plan Trip</button>


<div className="mt-8">
{itineraries.map(it=> (
<Itinerary key={it.option_id} itinerary={it} />
))}
</div>
</div>
)
}
