import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { AuthSlice } from "../../models/AuthSlice";

interface LoginProps {
  id: string;
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

export const authSlice = createSlice({
  name: "authSlice",
  initialState,
  reducers: {
    updateModal: (state, action: PayloadAction<boolean>) => {
      return { ...state, modalOpen: action.payload };
    },
    doLogin: (state, action: PayloadAction<LoginProps>) => {
      localStorage.setItem("username", action.payload.username);
      localStorage.setItem("id", action.payload.id ??"");
      return {
        ...state,
        username: action.payload.username,
        id: action.payload.id ?? "",
        modalOpen: false,
        isLoggedIn: true,
      };
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
