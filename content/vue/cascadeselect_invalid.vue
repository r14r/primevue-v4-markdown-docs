<div class="card flex flex-wrap justify-center gap-4">
    <CascadeSelect v-model="selectedCity1" :invalid="!selectedCity1" :options="countries" optionLabel="cname" optionGroupLabel="name" 
        :optionGroupChildren="['states', 'cities']" class="w-full sm:w-56" placeholder="Select a City" />
    <CascadeSelect v-model="selectedCity2" :invalid="!selectedCity2" :options="countries" optionLabel="cname" optionGroupLabel="name" 
        :optionGroupChildren="['states', 'cities']" class="w-full sm:w-56" placeholder="Select a City" variant="filled" />
</div>