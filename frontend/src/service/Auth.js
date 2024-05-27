import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000/";

export const login = async (body) => {
  return await axios.post(BASE_URL+"auth/user/login", body);
};