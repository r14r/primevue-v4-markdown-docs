<FloatLabel class="w-full md:w-56">
    <Select v-model="value1" inputId="over_label" :options="cities" optionLabel="name" class="w-full" />
    <label for="over_label">Over Label</label>
</FloatLabel>

<FloatLabel class="w-full md:w-56" variant="in">
    <Select v-model="value2" inputId="in_label" :options="cities" optionLabel="name" class="w-full" variant="filled" />
    <label for="in_label">In Label</label>
</FloatLabel>

<FloatLabel class="w-full md:w-56" variant="on">
    <Select v-model="value3" inputId="on_label" :options="cities" optionLabel="name" class="w-full" />
    <label for="on_label">On Label</label>
</FloatLabel>