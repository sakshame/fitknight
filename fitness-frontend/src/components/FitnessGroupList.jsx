import React, { useEffect, useState } from 'react';
import { getFitnessGroups } from '../services/api'; // Import the API function

const FitnessGroupList = () => {
  const [fitnessGroups, setFitnessGroups] = useState([]);

  useEffect(() => {
    const fetchFitnessGroups = async () => {
      try {
        const data = await getFitnessGroups();
        setFitnessGroups(data);
      } catch (error) {
        console.error('Failed to fetch fitness groups', error);
      }
    };

    fetchFitnessGroups();
  }, []);

  return (
    <div className="p-4 bg-white shadow-md rounded-lg">
      <h2 className="text-xl font-semibold mb-4">Fitness Group List</h2>
      <ul className="space-y-2">
        {fitnessGroups.map((group, index) => (
          <li key={index} className="flex justify-between items-center bg-gray-100 p-2 rounded-md">
            <span>{group.name}</span>
            <button className="px-4 py-2 bg-blue-500 text-white rounded-md">View</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default FitnessGroupList;
