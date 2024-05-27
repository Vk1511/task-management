import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000/";

export const getAllTask = async () => {
  const token = localStorage.getItem("accessToken");
  return await axios.get(BASE_URL + "task", {
    headers: { Authorization: `Bearer ${token}` },
  });
};

export const getAllComments = async (taskId) => {
  const token = localStorage.getItem("accessToken");
  return await axios.get(BASE_URL + `task/${taskId}/comment`, {
    headers: { Authorization: `Bearer ${token}` },
  });
};

export const updateTask = async (taskId, body) => {
  const token = localStorage.getItem("accessToken");
  return await axios.patch(BASE_URL + `task/${taskId}/`, body,{
    headers: { Authorization: `Bearer ${token}` },
  });
};


export const addTask = async (body) => {
  const token = localStorage.getItem("accessToken");
  return await axios.post(BASE_URL + `task/`, body,{
    headers: { Authorization: `Bearer ${token}` },
  });
};