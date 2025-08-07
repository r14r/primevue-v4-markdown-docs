<InputGroup>
    <Button label="Search" />
    <InputText placeholder="Keyword" />
</InputGroup>

<InputGroup>
    <InputText placeholder="Keyword" />
    <InputGroupAddon>
        <Button icon="pi pi-search" severity="secondary" variant="text" @click="toggle" />
    </InputGroupAddon>
</InputGroup>
<Menu ref="menu" :model="items" popup class="!min-w-fit" />

<InputGroup>
    <InputGroupAddon>
        <Button icon="pi pi-check" severity="secondary" />
    </InputGroupAddon>
    <InputText placeholder="Vote" />
    <InputGroupAddon>
        <Button icon="pi pi-times" severity="secondary" />
    </InputGroupAddon>
</InputGroup>