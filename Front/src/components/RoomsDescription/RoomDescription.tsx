import React, { useState } from 'react'
import './RoomDescription.scss'
import classNames from 'classnames'
import img1 from '../../resources/img/img1.jpg'
import img2 from '../../resources/img/img2.jpg'
import img3 from '../../resources/img/img3.jpg'

export const RoomDescription = () => {

  const [activeSlide, setActiveSlide] = useState(0)
  const data = [img1, img2, img3]

  const changeSlide = (condition: string) => {
    if (condition === 'prev') {
      activeSlide > 0 ? setActiveSlide(activeSlide - 1) : setActiveSlide(+(data.length - 1))
    }
    else if (condition === 'next') {
      activeSlide < (data.length - 1) ? setActiveSlide(1 + activeSlide) : setActiveSlide(0)
    }

  }

  return <>
    <div className="slideshow-container">
      <div className="mySlides fade">
        <h3>Выберите комнату</h3>
        {data.map((item, index) =>
        (<>
          <img src={String(item)} alt={''} className={classNames(`mySlides_`, { active: +activeSlide === +index })} />
          <div className="text">Caption Text</div>
        </>)
        )}
      </div> 
      <a className="prev"
        onClick={() => changeSlide('prev')}>&#10094;</a>
      <a className="next"
        onClick={() => changeSlide('next')}>&#10095;</a>
    </div>
    <br />

    {/*     <div>
      <span className="dot"></span>
      <span className="dot"></span>
      <span className="dot"></span>
    </div> */}
  </>
}
