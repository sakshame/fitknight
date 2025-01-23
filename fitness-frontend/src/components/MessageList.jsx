import React, { useEffect, useState } from 'react';
import { getMessages } from '../services/api'; // Import the API function

const MessageList = () => {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const fetchMessages = async () => {
      try {
        const data = await getMessages();
        setMessages(data);
      } catch (error) {
        console.error('Failed to fetch messages', error);
      }
    };

    fetchMessages();
  }, []);

  return (
    <div className="p-4 bg-white shadow-md rounded-lg">
      <h2 className="text-xl font-semibold mb-4">Messages</h2>
      <ul className="space-y-2">
        {messages.map((message, index) => (
          <li key={index} className="flex justify-between items-center bg-gray-100 p-2 rounded-md">
            <span>{message.content}</span>
            <button className="px-4 py-2 bg-blue-500 text-white rounded-md">View</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MessageList;
