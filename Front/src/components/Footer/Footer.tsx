import './Footer.scss';
import { Component } from 'react';
import svg_telegram from '../../resources/svg/telegram.svg';
import svg_whatsapp from '../../resources/svg/whatsapp_logo_icon.svg';

class Footer extends Component {
    state = {
        vis: false
    }

    visibilityMap = () => {
        this.setState({
            vis: !this.state.vis
        })
    }

    render() {
        return (
            <>
                <div className="footer_block" id="contacts">
                    <div className='footer_block_contacts'>
                        Номера для связи <br />
                        <div className='phoneNumber'><a href="tel:+78142332211" className='phoner_href'>+7(814)-233-22-11</a>  -  Контакт1<br /></div>
                        <div className='phoneNumber'><a href="tel:+78142332211" className='phoner_href'>+7(814)-233-22-11</a>  -  Контакт2</div>
                        <div className="icon">

                            <div className="icons _telegram">
                                <a href="https://tlgg.ru/vallug" target="blank">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" className="bi bi-telegram" viewBox="0 0 16 16">
                                        <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.287 5.906c-.778.324-2.334.994-4.666 2.01-.378.15-.577.298-.595.442-.03.243.275.339.69.47l.175.055c.408.133.958.288 1.243.294.26.006.549-.1.868-.32 2.179-1.471 3.304-2.214 3.374-2.23.05-.012.12-.026.166.016.047.041.042.12.037.141-.03.129-1.227 1.241-1.846 1.817-.193.18-.33.307-.358.336a8.154 8.154 0 0 1-.188.186c-.38.366-.664.64.015 1.088.327.216.589.393.85.571.284.194.568.387.936.629.093.06.183.125.27.187.331.236.63.448.997.414.214-.02.435-.22.547-.82.265-1.417.786-4.486.906-5.751a1.426 1.426 0 0 0-.013-.315.337.337 0 0 0-.114-.217.526.526 0 0 0-.31-.093c-.3.005-.763.166-2.984 1.09z" />
                                    </svg>
                                </a>
                                <a href="https://wa24.site/79510756629&text=Здравствуйте!%20У%20меня%20есть%20вопрос.%20" target="blank">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" className="bi bi-whatsapp" viewBox="0 0 16 16">
                                        <path d="M13.601 2.326A7.854 7.854 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.933 7.933 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.898 7.898 0 0 0 13.6 2.326zM7.994 14.521a6.573 6.573 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.557 6.557 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592zm3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.729.729 0 0 0-.529.247c-.182.198-.691.677-.691 1.654 0 .977.71 1.916.81 2.049.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z" />
                                    </svg>
                                </a>
                            </div>

                            <div className="icons _whatsapp">

                            </div>
                        </div>
                    </div>

                    <div className='footer_block_destination'>
                        <p onClick={this.visibilityMap}
                            className={this.state.vis ? "arrow_up" : "arrow_down"}>
                            Наше местоположение</p>
                        <div className={this.state.vis ? "footer_block_map" : "footer_block_map hide"}>
                            <iframe title='map'
                                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2039.5842727284949!2d39.58267303001949!3d43.70207486879613!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x40f431644102d4b7%3A0xde93d8e880288e75!2z0JvQvtC-LCDQodC-0YfQuCwg0JrRgNCw0YHQvdC-0LTQsNGA0YHQutC40Lkg0LrRgNCw0LksIDM1NDIwOA!5e0!3m2!1sru!2sru!4v1652465934229!5m2!1sru!2sru" width="400" height="300" loading="lazy" referrerPolicy="no-referrer-when-downgrade">
                            </iframe>
                        </div>
                    </div>
                </div>
            </>
        )
    }
}

export default Footer;