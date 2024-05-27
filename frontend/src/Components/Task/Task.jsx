import React, { useState } from "react";
import Navbar from "../Navbar/Navbar";
import { PlusOutlined } from "@ant-design/icons";
import { Button, Select, Modal, Input, DatePicker } from "antd";
import TaskContainer from "../TaskContainer/TaskContainer";
import dayjs from "dayjs";
import { addTask } from "../../service/task";
import "./Task.css";

const dateFormat = "YYYY-MM-DD";

export default function Task() {
  const [modal2Open, setModal2Open] = useState(false);
  const [title, setTitle] = useState(false);
  const [description, setDescription] = useState(false);
  const [date, setDate] = useState(false);
  const [hack,setHack] = useState(true);

  const handleChange = (value) => {
    console.log(`selected ${value}`);
  };

  const createTask = () => {
    console.log("object", title, description, date);
    addTask({
      "title": title,
      "description": description,
      "due_date": date
  }).then((res) => {
    setHack(false)
    }).catch((err) => {
      console.log("err",err)
    })
    setModal2Open(false);
  };

  return (
    <div>
      <Modal
        title="Vertically centered modal dialog"
        centered
        open={modal2Open}
        onOk={() => createTask()}
        onCancel={() => setModal2Open(false)}
      >
        <div>
          <b>Title:</b>{" "}
          <Input
            placeholder="title"
            onChange={(value) => setTitle(value.target.value)}
          />
        </div>
        <div>
          <b>Description:</b>{" "}
          <Input
            placeholder="Description"
            onChange={(value) => setDescription(value.target.value)}
          />
        </div>
        <div>
          <b>Due Date:</b>{" "}
          <DatePicker
            format={dateFormat}
            onChange={(date, dtstr) => setDate(dtstr)}
          />
        </div>
      </Modal>

      <Navbar />
      <div className="filters">
        <Select
          defaultValue="All"
          style={{
            width: 150,
            height: 40,
          }}
          onChange={handleChange}
          options={[
            {
              value: "All",
              label: "All",
            },
            {
              value: "Pending",
              label: "Pending",
            },
            {
              value: "In_Progress",
              label: "In Progress",
            },
            {
              value: "Done",
              label: "Done",
            },
          ]}
        />
        <Button
          icon={<PlusOutlined />}
          size="large"
          onClick={() => setModal2Open(true)}
        >
          Add Task
        </Button>
      </div>
      <TaskContainer hack={hack} />
    </div>
  );
}
