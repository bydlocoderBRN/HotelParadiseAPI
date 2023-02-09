import React from "react";
import './About.scss'
import img1 from '../../resources/img/try1.jpg'


export const About = () => {
    
    console.log(Number(Math.round(Number(-0.45 + 'e' + 1)) + 'e-' + 1).toFixed(2))
    return (
        <div className="about" id="aboutus">
            <h3>Что вас ждет?</h3>
            <div className="about__wrapper">
                <div className="about__wrapper-item">
                    <p className="one">Lorem ipsum dolor sit amet, consecte tur adipisic ing elit. Illo fugiat,Lorem
                        ipsum dolor sit amet consectetur adi pisicing elit. Reiciendis quidem moll itia expedita
                        a fugit ad minima quae similique nobis!</p>
                    <img src={img1} />
                </div>
                <div className="about__wrapper-item">
                    <img src={img1} />
                    <p className="one">Lorem ipsum dolor sit amet, consecte tur adipisic ing elit. Illo fugiat,Lorem
                        ipsum dolor sit amet consectetur adi pisicing elit. Reiciendis quidem moll itia expedita
                        a fugit ad minima quae similique nobis!</p>

                </div>
                <div className="about__wrapper-item">
                    <p className="one">Lorem ipsum dolor sit amet, consecte tur adipisic ing elit. Illo fugiat,Lorem
                        ipsum dolor sit amet consectetur adi pisicing elit. Reiciendis quidem moll itia expedita
                        a fugit ad minima quae similique nobis!</p>
                    <img src={img1} />
                </div>
            </div>
        </div>
    )
}