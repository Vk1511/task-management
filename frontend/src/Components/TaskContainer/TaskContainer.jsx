import React, { useEffect, useState } from "react";
import { Typography, Card } from "antd";
import { getAllTask } from "../../service/task";
import SelectedTask from "../SelectedTask/SelectedTask";
import "./TaskContainer.css";

const { Title } = Typography;

export default function TaskContainer({hack}) {
  const [taskCount, setTaskCount] = useState(0);
  const [pendingTask, setPendingTask] = useState([]);
  const [inProgresstask, setInProgressTask] = useState([]);
  const [doneTask, setDoneTask] = useState([]);
  const [selectedTaskDetails, setSelectedTaskDetails] = useState(null);
  const [patchSolve, setPatchSolve] = useState(true);

  const cardSelected = (cardDetails) => {
    setSelectedTaskDetails(cardDetails);
  };

  useEffect(() => {
    getAllTask()
      .then((res) => {
        const { task, total_task } = res?.data;
        const pending = task?.filter((task) => task.status === "PENDING");
        const inProgress = task?.filter(
          (task) => task.status === "IN PROGRESS"
        );
        const done = task?.filter((task) => task.status === "DONE");
        setTaskCount(total_task);
        setPendingTask(pending);
        setInProgressTask(inProgress);
        setDoneTask(done);
      })
      .catch((err) => {
        console.error(err);
      });
  }, [patchSolve, hack]);

  return (
    <>
      <div className="total">
        <Title level={3}>Total Task: {taskCount}</Title>
      </div>
      <div className="task-container">
        <div className="pending">
          <Title level={4}>Pending</Title>
          {pendingTask?.map((t) => {
            return (
              <Card
                key={t.id}
                title={t.title}
                extra={"Priority: " + t.priority}
                bordered={false}
                style={{
                  width: 300,
                  marginBottom: 8,
                  cursor: "pointer",
                }}
                onClick={() => cardSelected(t)}
              >
                <p>{t.description}</p>
                <p>Due Date: {t.due_date}</p>
                <p>Assigned to: {t.assigned_to}</p>
              </Card>
            );
          })}
        </div>
        <div className="in-progress">
          <Title level={4}>In Progress</Title>
          {inProgresstask?.map((t) => {
            return (
              <Card
                key={t.id}
                title={t.title}
                extra={"Priority: " + t.priority}
                bordered={false}
                style={{
                  width: 300,
                  marginBottom: 8,
                  cursor: "pointer",
                }}
                onClick={() => cardSelected(t)}
              >
                <p>{t.description}</p>
                <p>Due Date: {t.due_date}</p>
                <p>Assigned to: {t.assigned_to}</p>
              </Card>
            );
          })}
        </div>
        <div className="done">
          <Title level={4}>Done</Title>
          {doneTask?.map((t) => {
            return (
              <Card
                key={t.id}
                title={t.title}
                extra={"Priority: " + t.priority}
                bordered={false}
                style={{
                  width: 300,
                  marginBottom: 8,
                  cursor: "pointer",
                }}
                onClick={() => cardSelected(t)}
              >
                <p>{t.description}</p>
                <p>Due Date: {t.due_date}</p>
                <p>Assigned to: {t.assigned_to}</p>
              </Card>
            );
          })}
        </div>
        <div className="preview">
          <Title level={4}>Task Details</Title>
          {!selectedTaskDetails ? (
            <Title level={3}>Please Select any task for preview</Title>
          ) : (
            <SelectedTask
              task={selectedTaskDetails}
              setPatchSolve={setPatchSolve}
            ></SelectedTask>
          )}
        </div>
      </div>
    </>
  );
}
