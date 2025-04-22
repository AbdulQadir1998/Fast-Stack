import axios from "axios";

export const api = (token?: string) =>
  axios.create({
    baseURL: `${process.env.NEXT_PUBLIC_BACKEND_URL}/api`,
    headers: {
      Authorization: token ? `Bearer ${token}` : "",
    },
  });
  