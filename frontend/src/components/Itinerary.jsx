import React from 'react'


export default function Itinerary({itinerary}){
return (
<div className="border p-4 rounded my-4">
<h2 className="text-xl">Option {itinerary.option_id}</h2>
{itinerary.days.map(d=> (
<div key={d.date} className="mt-3">
<div className="font-semibold">{d.date}</div>
<ul>
{Object.entries(d.slots).map(([slot,val])=> (
<li key={slot}>{slot}: {val ? val.name : '—'}</li>
))}
</ul>
</div>
))}
</div>
)
}
