<FloatLabel>
    <AutoComplete v-model="value1" inputId="over_label" :suggestions="items" @complete="search" />
    <label for="over_label">Over Label</label>
</FloatLabel>

<FloatLabel variant="in">
    <AutoComplete v-model="value2" inputId="in_label" :suggestions="items" @complete="search" variant="filled" />
    <label for="in_label">In Label</label>
</FloatLabel>

<FloatLabel variant="on">
    <AutoComplete v-model="value3" inputId="on_label" :suggestions="items" @complete="search" />
    <label for="on_label">On Label</label>
</FloatLabel>