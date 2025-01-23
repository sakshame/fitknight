import axios from 'axios';

// Set up the base URL for the backend API (Django + DRF)
const API_URL = 'http://localhost:8000/sex/api'; // Replace with your actual Django backend URL if different

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Fetch users
export const getUsers = async () => {
  try {
    const response = await api.get('users/');
    return response.data;
  } catch (error) {
    console.error('Error fetching users:', error);
    throw error;
  }
};

// Fetch user by ID
export const getUserById = async (id) => {
  try {
    const response = await api.get(`users/${id}/`);
    return response.data;
  } catch (error) {
    console.error('Error fetching user by ID:', error);
    throw error;
  }
};

// Fetch workouts
export const getWorkouts = async () => {
  try {
    const response = await api.get('workouts/');
    return response.data;
  } catch (error) {
    console.error('Error fetching workouts:', error);
    throw error;
  }
};

// Fetch locations
export const getLocations = async () => {
  try {
    const response = await api.get('locations/');
    return response.data;
  } catch (error) {
    console.error('Error fetching locations:', error);
    throw error;
  }
};

// Fetch fitness groups
export const getFitnessGroups = async () => {
  try {
    const response = await api.get('fitness-groups/');
    return response.data;
  } catch (error) {
    console.error('Error fetching fitness groups:', error);
    throw error;
  }
};

// Fetch messages
export const getMessages = async () => {
  try {
    const response = await api.get('messages/');
    return response.data;
  } catch (error) {
    console.error('Error fetching messages:', error);
    throw error;
  }
};

// Fetch notifications
export const getNotifications = async () => {
  try {
    const response = await api.get('notifications/');
    return response.data;
  } catch (error) {
    console.error('Error fetching notifications:', error);
    throw error;
  }
};

// Fetch group activities
export const getGroupActivities = async () => {
  try {
    const response = await api.get('group-activities/');
    return response.data;
  } catch (error) {
    console.error('Error fetching group activities:', error);
    throw error;
  }
};
