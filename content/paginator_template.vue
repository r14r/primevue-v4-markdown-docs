<Paginator v-model:first="first" :rows="1" :totalRecords="12" template="FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink" />

<div class="p-4 text-center">
    <img :src="`https://primefaces.org/cdn/primevue/images/nature/nature${first + 1}.jpg`" :alt="first" class="rounded w-full sm:w-[30rem]" />
</div>