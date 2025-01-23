import React from 'react';
import UserList from '../components/UserList';
import WorkoutList from '../components/WorkoutList';

const Home = () => {
  return (
    <div>
      <h1 className="text-4xl font-bold text-center p-6">Welcome to FitKnight</h1>
      <UserList />
      <WorkoutList />
    </div>
  );
};

export default Home;
