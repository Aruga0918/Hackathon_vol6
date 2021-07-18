/* eslint-disable */
import mockServer from 'axios-mock-server'
import mock0 from './users/_userId'
import mock1 from './community/index'
import mock2 from './community/_communityId/join'

export default (client) => mockServer([
  {
    path: '/users/_userId',
    methods: mock0
  },
  {
    path: '/community',
    methods: mock1
  },
  {
    path: '/community/_communityId/join',
    methods: mock2
  }
], client, '')
