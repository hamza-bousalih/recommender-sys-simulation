import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { AuthSlice } from "../../models/AuthSlice";

interface LoginProps {
  username: string;
  password: string;
}

const initialState: AuthSlice = {
  isLoggedIn:
    localStorage.getItem("username") !== null &&
    localStorage.getItem("username") !== undefined &&
    localStorage.getItem("username") !== "" &&
    localStorage.getItem("id") !== null &&
    localStorage.getItem("id") !== undefined &&
    localStorage.getItem("id") !== "",
    modalOpen: false,
    username: localStorage.getItem("username") ?? "",
    id: localStorage.getItem("id") ?? "",
};

const users = [
  { id: 1, username: "user 1", password: "123" },
  { id: 2, username: "user 2", password: "123" },
  { id: 3, username: "user 3", password: "123" },
]

export const authSlice = createSlice({
  name: "authSlice",
  initialState,
  reducers: {
    updateModal: (state, action: PayloadAction<boolean>) => {
      return { ...state, modalOpen: action.payload };
    },
    doLogin: (state, action: PayloadAction<LoginProps>) => {
      if (
        users.some(u => u.username === action.payload.username && u.password === action.payload.password)
      ) {
        localStorage.setItem("username", action.payload.username);
        localStorage.setItem("id", users.find(u => u.username === action.payload.username)?.id.toString() ?? "");
        return {
          ...state,
          username: action.payload.username,
          id: users.find(u => u.username === action.payload.username)?.id.toString() ?? "",
          modalOpen: false,
          isLoggedIn: true,
        };
      } else {
        return state;
      }
    },
    doLogout: (state) => {
      localStorage.removeItem("username");
      localStorage.removeItem("id");
      return { ...state, username: "", isLoggedIn: false, id: "" };
    },
  },
});

export const { updateModal, doLogin, doLogout } = authSlice.actions;
export default authSlice.reducer;
