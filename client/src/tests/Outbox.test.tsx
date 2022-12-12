import React from 'react';
import { render, screen } from '@testing-library/react';
import OutboxBlock from '../pages/Outbox';

test('renders learn react link', () => {
  render(<OutboxBlock/>);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
