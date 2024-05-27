import React from "react";
import { Avatar, Dropdown } from "antd";
import { AntDesignOutlined, UserOutlined } from "@ant-design/icons";
import { Link } from "react-router-dom";
import "./Navbar.css";
import {useAuth} from "../../context/userContext";



export default function Navbar() {
  const {logout} = useAuth()

  const items = [
    {
      key: "1",
      label: (
          <Link
          to="/profile"
          style={{ textDecoration: "none" }}
        >Profile</Link>
      ),
    },
    {
      key: "2",
      label: (
          <div onClick={() => logout()}>Logout</div>
      ),
    },
  ];
  return (
    <div className="nav-con">
      <div className="nav-itm logo">Task Manager</div>
      <div className="nav-itm avtar">
        <Dropdown menu={{ items }} placement="bottomLeft">
          <Avatar
            style={{ backgroundColor: "#87d068" }}
            icon={<UserOutlined />}
          />
        </Dropdown>
      </div>
    </div>
  );
}
