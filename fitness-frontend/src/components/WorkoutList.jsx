import React, { useEffect, useState } from 'react';
import { getWorkouts } from '../services/api';

const WorkoutList = () => {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    getWorkouts()
      .then(response => {
        setWorkouts(response.data);
      })
      .catch(error => {
        console.error('Error fetching workouts:', error);
      });
  }, []);

  return (
    <div className="p-4">
      <h2 className="text-2xl font-bold mb-4">Workouts</h2>
      <ul className="space-y-4">
        {workouts.map(workout => (
          <li key={workout.id} className="bg-gray-100 p-4 rounded shadow">
            <p className="font-semibold">{workout.name}</p>
            <p>{workout.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default WorkoutList;
