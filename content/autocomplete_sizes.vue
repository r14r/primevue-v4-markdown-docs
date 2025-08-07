<AutoComplete v-model="value1" :suggestions="items" @complete="search" size="small" placeholder="Small" dropdown />
<AutoComplete v-model="value2" :suggestions="items" @complete="search" placeholder="Normal" dropdown />
<AutoComplete v-model="value3" :suggestions="items" @complete="search" size="large" placeholder="Large" dropdown />