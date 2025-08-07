<Inplace>
    <template #display>
        {{ text || 'Click to Edit' }}
    </template>
    <template #content="{ closeCallback }">
        <span class="inline-flex items-center gap-2">
            <InputText v-model="text" autofocus />
            <Button icon="pi pi-times" text severity="danger" @click="closeCallback" />
        </span>
    </template>
</Inplace>