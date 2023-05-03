import axios from "axios";

const CATEGORY_API_BASE_URL = "http://localhost:8000/category";

export const getCategories = () => {
  return axios.get(CATEGORY_API_BASE_URL);
}