

export const Calendar = () => {

    let now = new Date();

    var today = new Date();
    var lastDayOfMonth = new Date(today.getFullYear(), today.getMonth() + 1, 0).getDate;
    console.log(lastDayOfMonth)

    return (
        <>
            <div id="cal">
                <div className="header">
                    <span className="left button" id="prev"> &lang; </span>
                    <span className="left hook"></span>
                    <span className="month-year" id="label"> June 20&0 </span>
                    <span className="right hook"></span>
                    <span className="right button" id="next"> &rang; </span>
                </div>
                <table id="days">


                </table>
                <div id="cal-frame">


                </div>
            </div>

        </>
    )
}