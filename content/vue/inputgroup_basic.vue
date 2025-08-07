<InputGroup>
    <InputGroupAddon>
        <i class="pi pi-user"></i>
    </InputGroupAddon>
    <InputText v-model="text1" placeholder="Username" />
</InputGroup>

<InputGroup>
    <InputGroupAddon>$</InputGroupAddon>
    <InputNumber v-model="number" placeholder="Price" />
    <InputGroupAddon>.00</InputGroupAddon>
</InputGroup>

<InputGroup>
    <InputGroupAddon>www</InputGroupAddon>
    <InputText v-model="text2" placeholder="Website" />
</InputGroup>

<InputGroup>
    <InputGroupAddon>
        <i class="pi pi-map"></i>
    </InputGroupAddon>
    <Select v-model="selectedCity" :options="cities" optionLabel="name" placeholder="City" />
</InputGroup>