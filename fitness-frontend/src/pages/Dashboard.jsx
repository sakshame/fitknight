import React, { useEffect, useState } from 'react';
import { getWorkouts, getUsers, getLocations } from '../services/api'; // Import API functions
import LocationList from '../components/LocationList';
import FitnessGroupList from '../components/FitnessGroupList';
import MessageList from '../components/MessageList';

const Dashboard = () => {
  const [workouts, setWorkouts] = useState([]);
  const [users, setUsers] = useState([]);
  const [locations, setLocations] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const workoutsData = await getWorkouts();
        const usersData = await getUsers();
        const locationsData = await getLocations();
        setWorkouts(workoutsData);
        setUsers(usersData);
        setLocations(locationsData);
      } catch (error) {
        console.error('Failed to fetch dashboard data', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="p-8">
      <h1 className="text-3xl font-semibold mb-8">Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        {/* Pass the fetched data to the child components */}
        <LocationList locations={locations} />
        <FitnessGroupList users={users} />
      </div>
      {/* Pass the workouts data to MessageList or any other relevant component */}
      <MessageList workouts={workouts} />
    </div>
  );
};

export default Dashboard;
