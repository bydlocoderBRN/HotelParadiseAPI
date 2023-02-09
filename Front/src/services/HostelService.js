 class HostelService {
  
    apiKey = 'http://127.0.0.1:8081//room/all';

    getResource = async (url) => {
        let res = await fetch(url);
        if (!res.ok) {
            throw new Error(`Could not fetch ${url}, status: ${res.status}`);
        }
        return await res.json();
    }

    getRoom = async (id) => {
        const res = await this.getResource(`${this.apiKey}`);
        return this._transformRoom(res[id]);
    }

  _transformRoom = (char) => {
      
        return {
                id: char.id,
                description: char.description,
                price: {
                    start_date: char.start_date,
                    finish_date: char.finish_date,
                    price: char.price
                },
                links: [
                    {link: char.links[0].link},
                    {link: char.links[1].link},
                    {link: char.links[2].link},
                    {link: char.links[3].link},
                ]
    }  
 }
 }
 export default HostelService;

