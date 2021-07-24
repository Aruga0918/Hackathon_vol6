<template>
  <table class="table mb-0" style="border: none">
    <tbody>
      <tr class="align-middle">
        <td style="height: 70px; width: 70px">
          <b-img
            v-if="member.icon_url"
            :src="member.icon_url"
            style="
              object-fit: contain;
              border-radius: 50%;
              height: 70px;
              width: 70px;
            "
          />
          <b-img
            v-else
            :src="member.icon_url"
            style="
              object-fit: contain;
              border-radius: 50%;
              height: 70px;
              width: 70px;
            "
          />
        </td>
        <td class="align-middle">
          <div class="d-flex my-auto p-0" style="line-height: 0.5em">
            <h6 class="m-0">
              {{ member.name }}
            </h6>
            <small class="text-muted p-0 m-1">@{{ member.uid }}</small>
          </div>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  props: {
    member: {
      type: Object,
      required: true,
    },
  },
}
</script>
