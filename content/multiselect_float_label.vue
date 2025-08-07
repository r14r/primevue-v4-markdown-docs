<FloatLabel class="w-full md:w-80">
    <MultiSelect id="over_label" v-model="value1" :options="cities" optionLabel="name" filter :maxSelectedLabels="3" class="w-full" />
    <label for="over_label">Over Label</label>
</FloatLabel>

<FloatLabel class="w-full md:w-80" variant="in">
    <MultiSelect id="in_label" v-model="value2" :options="cities" optionLabel="name" filter :maxSelectedLabels="3" class="w-full" variant="filled" />
    <label for="in_label">In Label</label>
</FloatLabel>

<FloatLabel class="w-full md:w-80" variant="on">
    <MultiSelect id="on_label" v-model="value3" :options="cities" optionLabel="name" filter :maxSelectedLabels="3" class="w-full" />
    <label for="on_label">On Label</label>
</FloatLabel>