import React from 'react'
import { About } from '../About/About'
import './MainPage.scss'

export const MainPage = () => {
    return (
        <div className="mainpage">
            <div className="mainpage__wrapper">
                <ul className='mainpage__wrapper-menu'>
                    <li className='menu__item'>О нас</li>
                    <li className='menu__item'>Прайслист</li>
                    <li className='menu__item'>Комнаты</li>
                    <li className='menu__item'>Забронировать</li>
                    <li className='menu__item'>Контакты</li>

                </ul>
                <div className='block_main'>
                    <div className="block_main_content">
                        <h1>Гостевой дом</h1>
                        <h2 className='block_main_content_title'>"Рай"</h2>
                    </div>
                </div>
            </div>
            <About />
        </div>
    )
}