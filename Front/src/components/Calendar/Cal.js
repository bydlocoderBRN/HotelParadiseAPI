import React, { useState } from "react";

import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import { addDays } from 'date-fns';
import './Calendar.scss'

export const Cal = () => {
    const [startDate, setStartDate] = useState(new Date());
    const [endDate, setEndDate] = useState(null);
  const onChange = (dates) => {
    const [start, end] = dates;
    setStartDate(start);
    setEndDate(end);
  };

  return (
    <div className="cal">
    <DatePicker
      selected={startDate}
      onChange={onChange}
      startDate={startDate}
      endDate={endDate}
      excludeDates={[addDays(new Date(), 1), addDays(new Date(), 5), addDays(new Date(), 8), addDays(new Date(), 10)]}
      selectsRange
      selectsDisabledDaysInRange
      inline
    />
    </div>
  );
};
