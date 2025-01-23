import React, { useEffect, useState } from 'react';
import { getUsers } from '../services/api'; // Import the API function

const ProfilePage = () => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const data = await getUsers();
        setUser(data); // Assuming you want to display user info
      } catch (error) {
        console.error('Failed to fetch user data', error);
      }
    };

    fetchUser();
  }, []);

  if (!user) {
    return <div>Loading...</div>;
  }

  return (
    <div className="p-8">
      <h1 className="text-3xl font-semibold mb-8">Profile</h1>
      <div>
        <p>Name: {user.name}</p>
        <p>Email: {user.email}</p>
        {/* You can add other user data here */}
      </div>
    </div>
  );
};

export default ProfilePage;
