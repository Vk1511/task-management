import React, { useEffect, useState } from "react";
import { Typography, Select, DatePicker } from "antd";
import dayjs from "dayjs";
import { getAllComments, updateTask } from "../../service/task";
import "./SelectedTask.css";

const dateFormat = "YYYY/MM/DD";
const { Title } = Typography;

export default function SelectedTask({ task, setPatchSolve }) {
  const [comments, setComments] = useState([]);
  const [tampFix,setTampFix] = useState(true)
  const handleChange = (value) => {
    console.log(`selected ${value}`);
  };

  const {
    title,
    description,
    priority,
    status,
    due_date,
    is_public,
    created_at,
    updated_at,
    assigned_to,
    assigned_at,
    id,
  } = task;

  const handleStatusChange = (value) => {
    updateTask(id, { status: value })
      .then((res) => {
        setTampFix(!tampFix)
        setPatchSolve(!tampFix)
        console.log("object", res);
      })
      .catch((err) => {
        console.log(err);
      });
    console.log(`selected ${value}`);
  };

  useEffect(() => {
    getAllComments(id)
      .then((res) => {
        setComments(res?.data);
      })
      .catch((err) => {
        console.error(err);
      });
  }, [tampFix]);

  return (
    <div className="selected-task">
      <Title level={2}>{title}</Title>
      <div className="drops">
        <div>
          <b>Priorit:</b>{" "}
          <Select
            defaultValue={priority}
            style={{
              width: 120,
            }}
            onChange={handleChange}
            options={[
              {
                value: "HIGH",
                label: "High",
              },
              {
                value: "LOW",
                label: "Low",
              },
              {
                value: "MEDIUM",
                label: "Medium",
              },
            ]}
          />
        </div>
      </div>
      <div>
        <b>Status:</b>{" "}
        <Select
          defaultValue={status}
          style={{
            width: 120,
          }}
          onChange={handleStatusChange}
          options={[
            {
              value: "PENDING",
              label: "Pending",
            },
            {
              value: "IN PROGRESS",
              label: "In Progress",
            },
            {
              value: "DONE",
              label: "Done",
            },
          ]}
        />
      </div>

      <div>
        <b>Due Date:</b>{" "}
        <DatePicker
          defaultValue={dayjs(due_date, dateFormat)}
          format={dateFormat}
        />
      </div>

      <div>
        <b>Public:</b> {is_public ? "Yes" : "No"}
      </div>
      <div>
        <b>Created At:</b> {created_at}{" "}
      </div>
      <div>
        <b>Updated At:</b> {updated_at}
      </div>
      <div>
        <b>Assigned to:</b> {assigned_to}
      </div>
      <div>
        <b>Assigned at:</b> {assigned_at}
      </div>
      <div>
        <b>Description:</b>
      </div>
      <div>{description}</div>
      <div>
        <b>Comments:</b>
      </div>

      <div>
        {comments?.map((comment) => {
          return (
            <div className="comment" key={comment.id}>
              <div>{comment.comment}</div>
              <div className="grey">
                {comment.comment_by} - {comment.comment_at}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
