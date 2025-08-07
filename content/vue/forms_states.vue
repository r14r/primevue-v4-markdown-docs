<Form v-slot="$form" :initialValues :resolver @submit="onFormSubmit" class="grid lg:grid-cols-2 gap-4 w-full">
    <div class="flex flex-col justify-center items-center gap-4">
        <InputText name="username" type="text" placeholder="Username" class="w-full sm:w-56" />
        <Button type="submit" severity="secondary" label="Submit" class="w-full sm:w-56" />
    </div>
    <Fieldset legend="Form States" class="h-80 overflow-auto">
        <pre class="whitespace-pre-wrap">{{ $form }}</pre>
    </Fieldset>
</Form>