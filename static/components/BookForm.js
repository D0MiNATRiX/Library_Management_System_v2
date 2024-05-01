export default {
    template: `
    <div>
    <input type="text" placeholder="name" v-model="resource.name" />
    <input type="text" placeholder="content" v-model="resource.content" />
    <input type="text" placeholder="author" v-model="resource.author" />
    <input type="text" placeholder="date_issued" v-model="resource.date_issued" />
    <input type="text" placeholder="return_date" v-model="resource.return_date" />
    <button @click="createBook">Create Book</button> 
    </div>
    `,
    data() {
        return {
            resource: {
                name: null,
                content: null,
                author: null,
                date_issued: null,
                return_date: null
            },
            token: localStorage.getItem('auth-token')
        }
    },
    methods: {
        async createBook() {
            const res = await fetch('/api/book', {
                method: 'POST',
                headers: {
                    'Authentication-Token': this.token,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.resource)
            })
            const data = await res.json()
            if (res.ok) {
                alert(data.message)
            }
        }
    }
}