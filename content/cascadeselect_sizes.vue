<CascadeSelect v-model="value1" :options="countries" optionLabel="cname" optionGroupLabel="name" :optionGroupChildren="['states', 'cities']" 
    class="w-56" size="small" placeholder="Small" />
<CascadeSelect v-model="value2" :options="countries" optionLabel="cname" optionGroupLabel="name" :optionGroupChildren="['states', 'cities']" 
    class="w-56" placeholder="Normal" />
<CascadeSelect v-model="value3" :options="countries" optionLabel="cname" optionGroupLabel="name" :optionGroupChildren="['states', 'cities']" 
    class="w-56" size="large" placeholder="Large" />